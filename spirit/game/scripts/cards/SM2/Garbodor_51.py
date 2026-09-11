from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba5c7a2e-8954-5357-9fc5-d317f69c3d29',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name',
    display_name='Garbodor',
    searchable_by=['Garbodor', 'Stage 1', 'Garbodor'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name',
    family_id=568,
    abilities=[
        Attack(
            title='Trashalanche',
            game_text="This attack does 20 damage for each Item card in your opponent's discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Acid Spray',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
