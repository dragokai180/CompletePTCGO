from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d53564d-4288-5b3a-b351-ffec793e9c5c',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    display_name='Paldean Wooper',
    searchable_by=['Paldean Wooper', 'Basic', 'PaldeanWooper'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=194,
    abilities=[
        Attack(
            title='Splattering Poison',
            game_text='Both Active Pokémon are now Poisoned.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
