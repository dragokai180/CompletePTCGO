from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c70b49f7-5ea2-51ff-ac54-854a2822e57e',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name',
    display_name='Omastar',
    searchable_by=['Omastar', 'Stage 1', 'Omastar'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    family_id=138,
    abilities=[
        Ability(
            title='Restoring Beam',
            game_text='Once during your turn (before your attack), you may search your deck for a Restored Pokémon and put it onto your Bench. Shuffle your deck afterward.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
