from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='73e05f42-db9e-5351-90a8-0ae8be539e7c',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    display_name='Lampent',
    searchable_by=['Lampent', 'Stage 1', 'Lampent'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name',
    family_id=607,
    abilities=[
        Attack(
            title='Mirror Mirror',
            game_text='Each player either draws or discards cards until that player has 4 cards in his or her hand. (Your opponent does this first.)',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flickering Flames',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
