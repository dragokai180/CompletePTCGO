from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d740858-c383-5382-ba60-02a661354e67',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name',
    display_name='Zoroark',
    searchable_by=['Zoroark', 'Stage 1', 'Zoroark'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    family_id=570,
    abilities=[
        Attack(
            title='Taunt',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Night Punishment',
            game_text="This attack does 20 damage for each Pokémon in your discard pile. You can't do more than 200 damage in this way.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
