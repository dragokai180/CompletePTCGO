from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56eabe15-87a1-5789-a793-0f196fa74d72',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    display_name='Omanyte',
    searchable_by=['Omanyte', 'Stage 1', 'Omanyte'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=138,
    abilities=[
        Attack(
            title='Tickle',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
