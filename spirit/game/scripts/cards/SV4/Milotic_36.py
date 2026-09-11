from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8974cf3f-3357-5c1b-9a28-5a102245a98b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name',
    display_name='Milotic',
    searchable_by=['Milotic', 'Stage 1', 'Milotic'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    family_id=349,
    abilities=[
        Ability(
            title='Lifeboat',
            game_text='Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Each player puts a Basic Pokémon from their discard pile onto their Bench. (Your opponent puts a Basic Pokémon onto their Bench first.)',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hypno Splash',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
