from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0117edf5-cdd7-5916-983d-b368f2a5fd02',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    display_name='Frogadier',
    searchable_by=['Frogadier', 'Stage 1', 'Frogadier'],
    subtypes=['Stage 1'],
    collector_number=39,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Water Duplicates',
            game_text='Search your deck for up to 3 Frogadier and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
