from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='99cd467f-1468-5734-814d-68fe5bcd57d2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name',
    display_name='Chien-Pao',
    searchable_by=['Chien-Pao', 'Basic', 'ChienPao'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=1002,
    abilities=[
        Attack(
            title='Snow Bringer',
            game_text='Attach up to 2 Basic Water Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wrathful Blade',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
