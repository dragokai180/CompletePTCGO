from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba5ae52e-87e6-53b7-9e93-b113afefe123',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name',
    display_name='Torterra',
    searchable_by=['Torterra', 'Stage 2', 'Torterra'],
    subtypes=['Stage 2'],
    collector_number=10,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name',
    family_id=387,
    abilities=[
        Attack(
            title='Giga Drain',
            game_text='Remove from Torterra the number of damage counters equal to the damage you did to the Defending Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Land Crush',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
