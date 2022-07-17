using System.Data.SQLite;
using System.Diagnostics;

namespace bazPlanner.Models
{
    class Database
    {
        public static SQLiteConnection? connection;
        public static SQLiteCommand? command;
        //Create connection.
        static public bool Connect()
        {
            try
            {
                var connectionStringBuilder = new SQLiteConnectionStringBuilder();
                connectionStringBuilder.DataSource = "test.db";

                using (connection = new SQLiteConnection(connectionStringBuilder.ConnectionString))
                {
                    connection.Open();
                }
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
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM Owners WHERE OwnerName = '{OwnerName}' AND OwnerPass = '{OwnerPass}'"
            };
            int cnt = command.ExecuteReader().StepCount;
            return cnt;
        }
    }
}
