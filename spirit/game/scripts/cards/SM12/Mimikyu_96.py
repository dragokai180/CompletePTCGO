from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87d91eb3-2ccb-54b7-92f5-55ca62b8bb01',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name',
    display_name='Mimikyu',
    searchable_by=['Mimikyu', 'Basic', 'Mimikyu'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title='Impersonation',
            game_text='Discard a Supporter card from your hand. If you do, use the effect of that card as the effect of this attack.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mischievous Hands',
            game_text="Choose 2 of your opponent's Pokémon and put 2 damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
