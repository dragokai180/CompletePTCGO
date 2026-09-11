from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0743b903-04c3-578a-b29b-45b4a037699b',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    display_name='Torracat',
    searchable_by=['Torracat', 'Stage 1', 'Torracat'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    family_id=725,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
