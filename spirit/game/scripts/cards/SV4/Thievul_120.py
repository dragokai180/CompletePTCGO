from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='648ad775-90e5-572f-aa1f-caf260459c99',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name',
    display_name='Thievul',
    searchable_by=['Thievul', 'Stage 1', 'Thievul'],
    subtypes=['Stage 1'],
    collector_number=120,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name',
    family_id=827,
    abilities=[
        Ability(
            title="Rob-'n'-Run",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand, and then you choose 2 Energy cards you find there and shuffle them into your opponent's deck.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
