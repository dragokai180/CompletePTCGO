from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='13cd7e74-c8be-5b36-aa42-f687a828c644',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name',
    display_name='Regice',
    searchable_by=['Regice', 'Basic', 'Regice'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=378,
    abilities=[
        Ability(
            title='Iceberg Shield',
            game_text="If you have Regirock in play, prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Stage 2 Pokémon.",
            passive=standard_passive("If you have Regirock in play, prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Stage 2 Pokémon."),
        ),
        Attack(
            title='Frost Smash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
