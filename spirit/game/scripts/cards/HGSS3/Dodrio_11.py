from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='370d5137-3696-5a7b-9d9d-110abea75bb5',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name',
    display_name='Dodrio',
    searchable_by=['Dodrio', 'Stage 1', 'Dodrio'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    family_id=84,
    abilities=[
        Ability(
            title='Retreat Aid',
            game_text="As long as Dodrio is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("As long as Dodrio is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less."),
        ),
        Attack(
            title='Incessant Peck',
            game_text='Flip a coin until you get tails. This attack does 20 damage plus 20 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
