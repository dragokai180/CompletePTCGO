from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='9b421693-5bc8-51ef-9dc8-5ad0297c33bb',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froslassex.Name',
    display_name='Froslass ex',
    searchable_by=['Froslass ex', 'Stage 1', 'Tera', 'ex', 'Froslassex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=3,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    family_id=361,
    abilities=[
        Ability(
            title='Evanescent',
            game_text='If this Pokémon is in the Active Spot and is Knocked Out, flip a coin. If heads, your opponent takes 1 fewer Prize card.',
            passive=standard_passive('If this Pokémon is in the Active Spot and is Knocked Out, flip a coin. If heads, your opponent takes 1 fewer Prize card.'),
        ),
        Attack(
            title='Frost Bullet',
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
