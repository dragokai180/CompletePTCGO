from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94a6977f-b587-570d-9014-692268f1958a',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name',
    display_name='Alolan Marowak',
    searchable_by=['Alolan Marowak', 'Stage 1', 'AlolanMarowak'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=104,
    abilities=[
        Attack(
            title='Dance of Flames',
            game_text="For each Energy attached to your opponent's Pokémon, attach a Fire Energy card from your discard pile to your Pokémon in any way you like.",
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Burning Bonemerang',
            game_text="Flip 2 coins. This attack does 70 damage for each heads. If either of them is heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
