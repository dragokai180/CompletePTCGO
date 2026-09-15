from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b8317ad-f201-5ae2-bd2d-88c6423c9ca9',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ToxapexGX.Name',
    display_name='Toxapex-GX',
    searchable_by=['Toxapex-GX', 'Stage 1', 'GX', 'ToxapexGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=57,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    family_id=747,
    abilities=[
        Attack(
            title='Spike Cannon',
            game_text='Flip 4 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Super Intense Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 10 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=standard_attack,
        ),
        Attack(
            title='Total Shelter-GX',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=150,
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
