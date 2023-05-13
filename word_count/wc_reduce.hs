module Main where


count :: (String, Int) -> (String, Int) -> (String, Int)
count (k, acc) (_, v) = (k, acc + v)

main :: IO ()
main = do
    text <- getContents
    putStrLn $ pairToAns $ foldl1 count $ textToPairs text
    where
        pairToAns :: (String, Int) -> String
        pairToAns (k, v) = k ++ "\t" ++ show v

        textToPairs :: String -> [(String, Int)]
        textToPairs = map lineToPair . filter (not . null) . lines

        lineToPair :: String -> (String, Int)
        lineToPair line = (k, read v :: Int) where [k, v] = words line
