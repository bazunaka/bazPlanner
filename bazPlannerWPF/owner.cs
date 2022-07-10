using System;
using System.Data.SQLite;
using static bazPlannerWPF.DBConnect;

namespace bazPlannerWPF
{
    public class Owner
    {
        public string nameOwner;
        public string passwordOwner;

        public void AddToDatabase(string nameOwner, string passwordOwner)
        {
            InsertUser(nameOwner, passwordOwner);
        }
        static public void CheckAdmin()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = "SELECT * FROM owner WHERE name_owner='admin'"
            };
            int cnt = command.ExecuteReader().StepCount;
            if (cnt == 1)
            {
                auth form_auth = new auth();
                form_auth.Show();
            }
        }

        static public void Auth(string nameOwner, string passwordOwner)
        {           
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM owner WHERE name_owner='{nameOwner}' AND password_owner='{passwordOwner}'"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                Console.WriteLine("Success!");
            }
            else
            {
                Console.WriteLine("Abort!");
            }            
        }
    }
}
