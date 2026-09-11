from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8dd31885-e8a1-5585-855a-d64ea380ac84',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name',
    display_name='Slaking',
    searchable_by=['Slaking', 'Stage 2', 'Slaking'],
    subtypes=['Stage 2'],
    collector_number=83,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    family_id=287,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Knuckle Sandwich',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
