from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0447347f-5726-53e9-ac9f-cad4e7a77c41',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name',
    display_name='Mawile',
    searchable_by=['Mawile', 'Basic', 'Mawile'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title='Tight Jaw',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Cavernous Chomp',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
