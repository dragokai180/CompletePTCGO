from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6619d4c4-c003-5621-94af-589af3744202',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name',
    display_name='Tapu Lele',
    searchable_by=['Tapu Lele', 'Basic', 'TapuLele'],
    subtypes=['Basic'],
    collector_number=94,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=786,
    abilities=[
        Attack(
            title='Psywave',
            game_text="This attack does 20 damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Magical Swap',
            game_text="Move any number of damage counters on your opponent's Pokémon to their other Pokémon in any way you like.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
