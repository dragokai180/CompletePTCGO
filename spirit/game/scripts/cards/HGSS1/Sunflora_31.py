from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c14cf226-162a-558a-9618-bca38685f0e5',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name',
    display_name='Sunflora',
    searchable_by=['Sunflora', 'Stage 1', 'Sunflora'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name',
    family_id=191,
    abilities=[
        Ability(
            title='Sunshine Grace',
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Sunflora is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Blade Arms',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
