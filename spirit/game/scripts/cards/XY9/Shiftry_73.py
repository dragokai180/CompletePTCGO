from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e5b96c8-b6a0-55de-a1f6-bf9cfcb1c659',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name',
    display_name='Shiftry',
    searchable_by=['Shiftry', 'Stage 2', 'Shiftry'],
    subtypes=['Stage 2'],
    collector_number=73,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    family_id=273,
    abilities=[
        Attack(
            title='Roll Up',
            game_text="Flip 3 coins. If any of them are heads, your opponent reveals his or her hand. Then, for each heads, discard a card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Otherworldly Return',
            game_text='Put a Trainer card from your discard pile into your hand.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
