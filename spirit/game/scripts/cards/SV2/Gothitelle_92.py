from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='257d4731-bc04-5e81-877b-24255a407d1e',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name',
    display_name='Gothitelle',
    searchable_by=['Gothitelle', 'Stage 2', 'Gothitelle'],
    subtypes=['Stage 2'],
    collector_number=92,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name',
    family_id=574,
    abilities=[
        Ability(
            title='Read the Stars',
            game_text="Once during your turn, you may look at the top 2 cards of your opponent's deck and put 1 of them back. Put the other card on the bottom of their deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Psych Out',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
