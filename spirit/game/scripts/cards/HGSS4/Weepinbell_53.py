from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3130c563-2aa3-5761-88cb-79a48fe41daf',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    display_name='Weepinbell',
    searchable_by=['Weepinbell', 'Stage 1', 'Weepinbell'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Poisonpowder',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corrode Target',
            game_text="Flip a coin. If heads, look at your opponent's hand, choose 1 card, and discard it.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
