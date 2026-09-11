from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8b877418-8b41-5036-9c28-96b34b067e11',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name',
    display_name='Honchkrow',
    searchable_by=['Honchkrow', 'Stage 1', 'Honchkrow'],
    subtypes=['Stage 1'],
    collector_number=130,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    family_id=198,
    abilities=[
        Attack(
            title='Sharpshooting',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dark Cutter',
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
        ),
    ],
)
