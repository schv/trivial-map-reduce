module Main where

import Data.Char (toLower, isAlpha)

cleanup :: String -> String
cleanup = (map toLower) . (filter isAlpha)

tokenize :: String -> [String]
tokenize = filter (not . null) . map cleanup . words

main :: IO ()
main = do
    text <- getContents
    mapM_ (putStrLn . (++ "\t1")) $ tokenize text
