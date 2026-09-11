from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aaed765d-956f-5045-a984-833ea6e38df1',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name',
    display_name='Banette',
    searchable_by=['Banette', 'Stage 1', 'Banette'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    family_id=353,
    abilities=[
        Attack(
            title='Lost Crush',
            game_text="Flip a coin. If heads, choose 1 Energy card attached to 1 of your opponent's Pokémon and put it in the Lost Zone.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Breakdown',
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
