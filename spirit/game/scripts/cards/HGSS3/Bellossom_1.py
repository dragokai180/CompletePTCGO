from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c33de55d-699c-5082-b1ae-7c15c0d7ad66',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name',
    display_name='Bellossom',
    searchable_by=['Bellossom', 'Stage 2', 'Bellossom'],
    subtypes=['Stage 2'],
    collector_number=1,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Hustle Step',
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from each of your Pokémon. This power can't be used if Bellossom is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Dance 'til Dawn",
            game_text='Flip 3 coins. This attack does 30 damage times the number of heads. Bellossom is now Asleep.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
