from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df860e71-0153-55c1-abf7-b8225be909be',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMukGX.Name',
    display_name='Alolan Muk-GX',
    searchable_by=['Alolan Muk-GX', 'Stage 1', 'GX', 'AlolanMukGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=84,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    family_id=88,
    abilities=[
        Attack(
            title='Chemical Breath',
            game_text="This attack does 70 more damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Tri Hazard-GX',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Burned, Paralyzed, and Poisoned. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
