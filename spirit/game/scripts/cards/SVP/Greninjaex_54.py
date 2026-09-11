from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dac0776f-caec-5559-a3b1-71c380bc7146',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name',
    display_name='Greninja ex',
    searchable_by=['Greninja ex', 'Stage 2', 'ex', 'Greninjaex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=54,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=658,
    abilities=[
        Attack(
            title='Stealthy Shuriken',
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Torrential Slash',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
