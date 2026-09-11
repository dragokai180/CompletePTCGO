from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='093bbe28-2f07-573f-a308-b4fddb59d910',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name',
    display_name='Hypno',
    searchable_by=['Hypno', 'Stage 1', 'Hypno'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    family_id=96,
    abilities=[
        Attack(
            title='Hand Control',
            game_text='Your opponent reveals his or her hand. You may choose a Supporter card you find there. If you do, your opponent plays that Supporter card. However, you make all decisions for that card. (That Supporter card is discarded.)',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
