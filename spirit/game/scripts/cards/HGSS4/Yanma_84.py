from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='589e8c33-3e2a-5400-bb49-fc866fcd9577',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    display_name='Yanma',
    searchable_by=['Yanma', 'Basic', 'Yanma'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=193,
    abilities=[
        Ability(
            title='Free Flight',
            game_text="If Yanma has no Energy attached to it, Yanma's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("If Yanma has no Energy attached to it, Yanma's Retreat Cost is 0."),
        ),
        Attack(
            title='Dive',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
