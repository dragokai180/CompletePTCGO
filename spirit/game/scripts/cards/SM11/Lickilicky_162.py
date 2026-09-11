from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e27cdec4-fdd4-5dfe-9bc1-023c7e582f9c',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name',
    display_name='Lickilicky',
    searchable_by=['Lickilicky', 'Stage 1', 'Lickilicky'],
    subtypes=['Stage 1'],
    collector_number=162,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    family_id=108,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Licks Go Crazy',
            game_text="Discard a random card from your opponent's hand, discard the top card of your opponent's deck, and discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
