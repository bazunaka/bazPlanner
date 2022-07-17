using System.Data.SQLite;
using System.Diagnostics;

namespace bazPlanner.Models
{
    class Database
    {
        public static SQLiteConnection connection;
        public static SQLiteCommand command;
        //Create connection.
        static public bool Connect()
        {
            try
            {
                connection = new SQLiteConnection("Data Source=test.db; Version=3; FailIfMissing=False");
                connection.Open();
                Debug.WriteLine("Connected!");
                return true;
            }
            catch (SQLiteException ex)
            {
                Debug.WriteLine($"Ошибка доступа к базе данных. Исключение: {ex.Message}");
                return false;
            }
            
        }
        
        //Select owner for auth.
        static public int SelectOwner(string OwnerName, string OwnerPass)
        {
            string nameLower = OwnerName.ToLower();
            string passLower = OwnerPass.ToLower(); 
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM Owners WHERE OwnerName = '{nameLower}' AND OwnerPass = '{passLower}'"
            };
            int cnt = command.ExecuteReader().StepCount;
            return cnt;
        }
    }
}
