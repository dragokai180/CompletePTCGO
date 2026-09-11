from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='987c3c8f-41ee-55b1-b887-1f5817c04335',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RegirockEX.Name',
    display_name='Regirock-EX',
    searchable_by=['Regirock-EX', 'Basic', 'EX', 'RegirockEX'],
    subtypes=['Basic', 'EX'],
    collector_number=43,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=377,
    abilities=[
        Ability(
            title='Regi Power',
            game_text="The attacks of your Fighting Pokémon (excluding Regirock-EX) do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("The attacks of your Fighting Pokémon (excluding Regirock-EX) do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Bedrock Press',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
