from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b284770e-abbc-55aa-b656-96db7728735b',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name',
    display_name='Tyranitar',
    searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Spinning Tail',
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Bite Off',
            game_text="If your opponent's Active Pokémon is a Pokémon-GX or a Pokémon-EX, this attack does 100 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
