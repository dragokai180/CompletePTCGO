from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3cf9e7e6-64b6-59bd-8530-c2ce2cbdf16b',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name',
    display_name='Purugly',
    searchable_by=['Purugly', 'Stage 1', 'Purugly'],
    subtypes=['Stage 1'],
    collector_number=109,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name',
    family_id=431,
    abilities=[
        Attack(
            title='Own the Place',
            game_text="If your opponent has a Stadium card in play, discard it. If you do, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Toss Aside',
            game_text="Discard random cards from your opponent's hand until they have 3 cards in their hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
