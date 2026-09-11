from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df322d25-85b3-5b93-8354-342a36217add',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name',
    display_name='Cherrim',
    searchable_by=['Cherrim', 'Stage 1', 'Cherrim'],
    subtypes=['Stage 1'],
    collector_number=28,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name',
    family_id=420,
    abilities=[
        Ability(
            title='Sunny Heal',
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from your Active Pokémon. This power can't be used if Cherrim is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
