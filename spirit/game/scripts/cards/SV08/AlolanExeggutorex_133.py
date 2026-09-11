from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="62c4a44c-f101-523d-9d64-76507dbd3dcd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorex.Name",
    display_name="Alolan Exeggutor ex",
    searchable_by=["Alolan Exeggutor ex", "Stage 1", "Tera", "ex", "AlolanExeggutorex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=133,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Frenzy",
            game_text="You may attach any number of Basic Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title="Swinging Sphene",
            game_text="Flip a coin. If heads, Knock Out your opponent's Active Basic Pokémon. If tails, Knock Out 1 of your opponent's Benched Basic Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
