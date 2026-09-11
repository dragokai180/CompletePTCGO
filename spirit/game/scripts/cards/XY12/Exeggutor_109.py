from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8bcd190f-c582-5574-b079-f2a1a62192c4',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name',
    display_name='ナッシー[Exeggutor]',
    searchable_by=['ナッシー[Exeggutor]', 'Stage 1', 'Exeggutor'],
    subtypes=['Stage 1'],
    collector_number=109,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=103,
    abilities=[
        Attack(
            title='ふみつけ[Stomp]',
            game_text='コインを1回投げオモテなら、10ダメージを追加。 Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
