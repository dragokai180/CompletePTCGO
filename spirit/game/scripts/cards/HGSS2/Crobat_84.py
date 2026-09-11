from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='73dcd1af-71f0-5a4c-90e5-3fc049281226',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name',
    display_name='Crobat',
    searchable_by=['Crobat', 'Stage 2', 'Prime', 'Crobat'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=84,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Severe Poison',
            game_text='The Defending Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon between turns.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Skill Dive',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
