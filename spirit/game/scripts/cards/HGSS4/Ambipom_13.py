from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37744d70-058e-561e-9355-b86b57753088',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name',
    display_name='Ambipom',
    searchable_by=['Ambipom', 'Stage 1', 'Ambipom'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name',
    family_id=190,
    abilities=[
        Attack(
            title='Astonish',
            game_text="Choose 2 cards from your opponent's hand without looking. Look at the cards you chose, then have your opponent shuffle those cards into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Tail Spank',
            game_text="Discard 2 cards from your hand. (If you can't discard 2 cards from your hand, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
