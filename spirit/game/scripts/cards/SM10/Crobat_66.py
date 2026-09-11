from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3539237a-40af-5b43-b834-4094f33d6b8a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name',
    display_name='Crobat',
    searchable_by=['Crobat', 'Stage 2', 'Crobat'],
    subtypes=['Stage 2'],
    collector_number=66,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    family_id=41,
    abilities=[
        Ability(
            title='Sound Veil',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may prevent all effects of your opponent's attacks, including damage, done to this Pokémon until the end of your opponent's next turn.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Severe Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
