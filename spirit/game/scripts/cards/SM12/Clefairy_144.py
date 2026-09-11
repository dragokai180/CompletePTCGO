from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ead9f49e-226a-58e2-b480-f7f7d936a287',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    display_name='Clefairy',
    searchable_by=['Clefairy', 'Basic', 'Clefairy'],
    subtypes=['Basic'],
    collector_number=144,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title='Doll Swap',
            game_text="Put this Pokémon and all cards attached to it into your hand. If you do, you may play Lillie's Poké Doll from your hand as your new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
