from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bb7e325-76f1-5b00-8b21-2f5ea1024c1b',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name',
    display_name='Alolan Exeggutor',
    searchable_by=['Alolan Exeggutor', 'Stage 1', 'AlolanExeggutor'],
    subtypes=['Stage 1'],
    collector_number=114,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Attack(
            title='Tropical Shake',
            game_text="This attack does 20 more damage for each type of basic Energy card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
