from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0fa0835-0507-57b9-8f4b-75cf45e3cc0e',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name',
    display_name='Bewear',
    searchable_by=['Bewear', 'Stage 1', 'Bewear'],
    subtypes=['Stage 1'],
    collector_number=182,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=759,
    abilities=[
        Ability(
            title='Carry and Run',
            game_text="As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less.",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less."),
        ),
        Attack(
            title='Lariat',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
