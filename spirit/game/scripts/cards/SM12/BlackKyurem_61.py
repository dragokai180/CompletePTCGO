from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7097af38-dc1e-50ab-b6c7-7b4f58fe2da2',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name',
    display_name='Black Kyurem',
    searchable_by=['Black Kyurem', 'Basic', 'BlackKyurem'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Frozen Wings',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dazzling Blizzard',
            game_text='If you have any Stadium card in play, this attack does 100 more damage.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
