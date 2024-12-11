<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Save settings for pointer lists such as Dock, Stickies, CountdownTimerPlus etc. and restore them later in case they are lost following an update or a restart or a crash 
</title>
</head>
<body>
    <h1>Save those annoying Plists with a single command</h1>
    <button id="clickMe">Click Me!</button>
    <p id="output"></p>

    <script>
        document.getElementById("clickMe").addEventListener("click", () => {
            document.getElementById("output").textContent = "Button Clicked!";
        });
    </script>
</body>
</html>

