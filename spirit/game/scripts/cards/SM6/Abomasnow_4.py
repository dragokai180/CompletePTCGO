from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='728eb2d7-e413-5242-b37f-1d3f5bb45204',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name',
    display_name='Abomasnow',
    searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    family_id=459,
    abilities=[
        Ability(
            title='Blessings of the Frost',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may attach a Grass Energy card from your discard pile to 1 of your Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Hypno Hammer',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
